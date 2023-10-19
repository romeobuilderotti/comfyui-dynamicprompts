from dynamicprompts.generators import FeelingLuckyGenerator, RandomPromptGenerator

from .generator import DPGeneratorNode


class DPFeelingLucky(DPGeneratorNode):
    def generate_prompt(self, text, seed, wildcard_pipe) -> str:
        prompt_generator = FeelingLuckyGenerator(generator=RandomPromptGenerator(seed=seed, wildcard_manager=wildcard_pipe))

        all_prompts = prompt_generator.generate(text, 1) or [""]
        return all_prompts[0]
