from dynamicprompts.generators import JinjaGenerator

from .generator import DPGeneratorNode


class DPJinja(DPGeneratorNode):
    def generate_prompt(self, text, seed, wildcard_pipe):
        # TODO: Add seed support
        prompt_generator = JinjaGenerator(wildcard_manager=wildcard_pipe)

        all_prompts = prompt_generator.generate(text, 1) or [""]
        return all_prompts[0]
