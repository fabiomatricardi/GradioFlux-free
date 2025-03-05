# GradioFlux-free
A Gradio Image Generation with Flulx.1-Schnell and [together.ai](https://api.together.ai/) free API

The Gradio Interface that complete my other[ GitHub Rpository](https://github.com/fabiomatricardi/FLUX1-Schenll_TAI-freeAPI/blob/main/README.md)


<img src='https://github.com/fabiomatricardi/GradioFlux-free/raw/main/FluxGRADIO.png' width=900>

> portrait | wide angle shot of eyes off to one side of frame, lucid dream-like 3d model of owl, game asset, blender, looking off in distance ::8 style | glowing ::8 background | forest, vivid neon wonderland, particles, blue, green, orange ::7 parameters | rule of thirds, golden ratio, assymetric composition, hyper- maximalist, octane render, photorealism, cinematic realism, unreal engine, 8k ::7 --ar 16:9 --s 1000

---

Together AI provide free access with API to Top Notch models.

## Flux.1-Schenll is awesome at very small Steps (even only 1 or 4)

Flux.1-Schenll can be used for free (siwth some limitations)
- remotely with an API Key
- on the web with https://api.together.ai/

Free quota:
- 10 Requests Per Minute
- Total 60.000 requests per Months

Register at https://api.together.ai/


### What is Flux.1-Schnell
FLUX.1-Schnell is a 12 billion parameter rectified flow transformer designed to generate high-quality images from text descriptions. It is trained using latent adversarial diffusion distillation, which allows it to produce images in just 1 to 4 steps. This model is optimized for speed and efficiency, making it suitable for both personal and commercial use. 

It is available under an Apache 2.0 license, and its implementation and sampling code can be found in a dedicated GitHub repository. FLUX.1-Schnell can be used to create a variety of images, including photorealistic scenes, artistic illustrations, and concept art, applicable to diverse applications.

FLUX.1-Schnell can produce images in only 4 steps due to its training methodology and architecture. Here are the key factors that enable this efficiency:

- Latent Adversarial Diffusion Distillation: This training technique allows the model to generate high-quality images with fewer steps compared to traditional diffusion models. It distills the knowledge from a larger, more complex model into a smaller, more efficient one, enabling faster inference.
- Rectified Flow Transformer Architecture: The model's architecture is designed to optimize the flow of information during the generation process. This includes a hybrid architecture that combines multimodal and parallel diffusion transformer blocks, enhancing both speed and quality.
- Optimized Inference: The model includes optimizations such as compiled fp8 quantization and optimized attention kernels, which further accelerate the image generation process. These optimizations are crucial for achieving high-quality outputs in fewer steps.

#### Note
> You cannot set more than 4 steps in the generation!

## Generation results

> PROMPT: Depict a cozy, warmly lit bookstore cafe on a rainy evening. The atmosphere should be inviting and nostalgic, with soft yellow lighting from vintage lamps illuminating rows of well-worn books. Show patrons reading in comfortable armchairs, steam rising from their coffee cups. The large front window should reveal a glistening wet street outside, with blurred lights from passing cars. Emphasize the contrast between the warm interior and the cool, rainy exterior.

Here the few examples (1 step on the left, 4 steps on the right)

<img src='https://github.com/fabiomatricardi/FLUX1-Schenll_TAI-freeAPI/raw/main/interior-1step.png' width=450> <img src='https://github.com/fabiomatricardi/FLUX1-Schenll_TAI-freeAPI/raw/main/interior-4steps.png' width=450>

---

Remote calls requires the Together package. Recommended to use Python 3.12 to avoid dependency clashes
```
pip install together==1.4.1 gradio
```

Or Clone the repo and create a venv and install from requirements
```
python312 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

To run the generation:
```
gradio Gradio_Flux.py
```
You will be asked for:
- a valid API key
- a prompt


### Some prompt examples
You can find more [here](https://getimg.ai/blog/flux-1-prompt-guide-pro-tips-and-common-mistakes-to-avoid) and [here](https://aimlapi.com/blog/master-the-art-of-ai-top-10-prompts-for-flux-1-by-black-forests-labs)


> A hanging glass terrarium featuring a miniature rainforest scene with colorful orchids and tiny waterfalls. Just beyond the glass, a neon sign reads 'Rainforest Retreat.' The rain-soaked glass creates a beautiful distortion, adding a soft glow to the sign's vibrant colors - [from source](https://www.3daistudio.com/blog/the-best-flux-black-forest-labs-prompts-for-good-results-in-ai-image-generation)

<img src='https://github.com/fabiomatricardi/FLUX1-Schenll_TAI-freeAPI/raw/main/terrarium.png' height=400> 


---


> Photo realistic scene inspired by LOTR: [A tiny red dragon sleeps curled up in a nest on a medieval wizard's table]. Shot with a macro lens (f/2.8, 50mm) and a Canon EOSR5, the soft focus captures [the cozy morning light filtering through a near by window]. The pastel colors and whimsical steam shapes enhance the serene atmosphere, evoking a DnD RPG setting. The image is rendered in 16K and 8K, highlighting [the intricate details and medieval charm].

<img src='https://github.com/fabiomatricardi/FLUX1-Schenll_TAI-freeAPI/raw/main/dragon.png' height=400>

---


> A single tree standing in the middle of the image. The left half of the tree has bright, vibrant red leaves under a bright, sunny blue sky, while the right half has bare branches covered in frost, with a cold, dark, thunderous sky. On the left there's orange, lush grass on the ground; on the right - thick snow. The split is sharp, with the transition happening right down the middle of the tree

<img src='https://github.com/fabiomatricardi/FLUX1-Schenll_TAI-freeAPI/raw/main/red-whiteTREE.png' height=400>


---

## Resources
- Together AI [pypi package page](https://pypi.org/project/together/)
- [Together.AI](https://api.together.ai/)
- [Introduction](https://docs.together.ai/docs/introduction) to TogetherAI and services
- [Together.Cookbooks](https://github.com/togethercomputer/together-cookbook)
- How to create Images - [QuickStart](https://docs.together.ai/docs/images-overview)
- other [amazing prompts](https://www.3daistudio.com/blog/the-best-flux-black-forest-labs-prompts-for-good-results-in-ai-image-generation)


---



