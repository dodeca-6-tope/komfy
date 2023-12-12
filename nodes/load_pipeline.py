from diffusers import AutoPipelineForText2Image
import torch


class LoadPipeline:
    def run(model):
        return AutoPipelineForText2Image.from_pretrained(
            model, torch_dtype=torch.float16, variant="fp16"
        ).to("mps")
