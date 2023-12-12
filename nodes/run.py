class Run:
    def run(pipeline, prompt):
        return pipeline(prompt).images[0]
