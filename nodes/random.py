from dynamicprompts.generators import RandomPromptGenerator

from .generator import DPGeneratorNode


class DPRandomGenerator(DPGeneratorNode):
    def generate_prompt(self, text, seed, wildcard_manager) -> tuple[str]:
        prompt_generator = RandomPromptGenerator(seed=seed, wildcard_manager=wildcard_manager)

        all_prompts = prompt_generator.generate(text, 1) or [""]
        return all_prompts[0]