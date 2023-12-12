from engine import run


def create_test_workflow(prompt, output_path):
    return {
        "0": {
            "module": "load_pipeline",
            "node": "LoadPipeline",
            "args": {
                "model": "runwayml/stable-diffusion-v1-5",
            },
        },
        "1": {
            "module": "run",
            "node": "Run",
            "args": {
                "pipeline": "$0",
                "prompt": prompt,
            },
        },
        "2": {
            "module": "save",
            "node": "Save",
            "args": {
                "image": "$1",
                "output_path": output_path,
            },
        },
    }


run(workflow=create_test_workflow(prompt="cat", output_path="cat.png"), output_node="2")
run(workflow=create_test_workflow(prompt="dog", output_path="dog.png"), output_node="2")
