"""
20250305 
"""
import random, string
import gradio as gr
from rich.console import Console
import os
from datetime import datetime
from PIL import Image
from PIL.PngImagePlugin import PngInfo
from together import Together
import requests
from PIL import Image
from io import BytesIO


def genRANstring(n):
    """
    n = int number of char to randomize
    Return -> str, the filename with n random alphanumeric charachters
    """
    N = n
    res = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k=N))
    print(f'IM-{res}.png  CREATED')
    return f'IM-{res}.png'


console = Console(width=80)
theme=gr.themes.Default(primary_hue="blue", secondary_hue="pink",
                        font=[gr.themes.GoogleFont("Lato"), "Arial", "sans-serif"]) 

def openDIR():
    """
    Open the current working directory in windows explorer
    """
    import os
    current_directory = os.getcwd()
    print("Current Directory:", current_directory)
    os.system(f'start explorer "{current_directory}"')

def checkHFT(hf_token):
    if 'hf_' in hf_token:
        return gr.Row(visible=True),gr.Row(visible=True),gr.Row(visible=True),gr.Row(visible=True),"✅HF TOKEN detected"
   
    else:
        gr.Warning("⚠️ You don't have a Hugging Face Token set")
  

############### CREATE IMAGE ##########################
def CreateImage(PROMPT,APIK,STEPS,WIDTH,HEIGHT):
    """
    Use in terminal sd.exe stable diffusion cpp to create an image from a given prompt, and then it displays it in the gradio app
    PROMPT -> str, with no line brakes.
    STEPS - > int, number of sample steps for the diffuser
    WIDTH,HEIGHT -> int, image dimensions: must be multiples of 64 the bigger the image, the bigger the VRAM requirements and generation time
    Returns:
    targetimage -> PIL object 
    fILENAME -> str, filename of the image
    """
    if APIK =='':
        gr.Warning("⚠️ You don't have a Together.ai Token set")
        return targetimage, fILENAME
    else:
        fILENAME = genRANstring(5)
        print(f'Generating image with Flux.1-Schnell as: {fILENAME}')
        start = datetime.now()
        client = Together(api_key=APIK)
        response = client.images.generate(prompt=PROMPT,
                                          model="black-forest-labs/FLUX.1-schnell-Free", 
                                          steps=STEPS, 
                                          width=WIDTH, height=HEIGHT,n=1)
        imurl = response.data[0].url
        my_res = requests.get(imurl)
        my_img = Image.open(BytesIO(my_res.content))
        my_img.save(fILENAME)
        delta = datetime.now() - start
        # SAVE METADATA
        metadata = PngInfo()
        metadata.add_text("Flux.1-Schnell Prompt", PROMPT)
        metadata.add_text("ImageSize", f'WxH: {WIDTH} x {HEIGHT}')
        metadata.add_text("Steps", f'Steps: {STEPS} Sampling Method: euler')
        metadata.add_text("GenerationTime", f'{str(delta)}')
        targetimage = Image.open(fILENAME)
        targetimage.save(fILENAME,pnginfo=metadata) 
        # FINALLY SHOW THE IMAGE               
        print(f'Saving the Generated image with Flux.1-Schnell as: {fILENAME}')
        print(f'Completed in {delta}')
        targetimage = Image.open(fILENAME)
        return targetimage, fILENAME

with gr.Blocks(fill_width=True,theme=theme) as demo:
    # INTERFACE
    with gr.Row(variant='panel'):
        gr.HTML(
        f"""<h1 style="text-align:center">Generate images with Flux.1-Schnell</h1>""")       
    with gr.Row():
        #HYPERPARAMETERS
        with gr.Column(scale=1):
            TOKEN = gr.Textbox(lines=1,label='API KEY',scale=1,info='Togheter AI API key')
            gr.Markdown('---')
            i_steps = gr.Slider(minimum=1,maximum=4,value=4,step=1,label='Steps')
            i_width = gr.Slider(minimum=64,maximum=1024,value=1024,step=64,label='Width')
            i_height = gr.Slider(minimum=64,maximum=1024,value=1024,step=64,label='Height')
            GEN_IMAGE = gr.Button(value='Generate Image',variant='primary')
            gr.Markdown('---')
            ImageFilename = gr.Textbox(lines=2,
                                       label='Generated Image Filename',
                                       show_copy_button=True)
            OPEN_FOLDER = gr.Button(variant='secondary',value='Open Image Folder')
            clear = gr.ClearButton()
        with gr.Column(scale=3):
            SDPrompt = gr.Textbox(lines=8,label='FLUX.1-SCHENLL PROMPT')
            SDImage = gr.Image(type='pil',
                               label='Generated Image',
                               show_download_button=True, 
                               show_fullscreen_button=True,)
                   
    GEN_IMAGE.click(CreateImage,[SDPrompt,TOKEN,i_steps,i_width,i_height],[SDImage,ImageFilename])
    OPEN_FOLDER.click(openDIR,[],[])


if __name__ == "__main__":
    demo.launch()   

