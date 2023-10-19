from abc import ABC, abstractmethod

from .wildcard_pipe import PipeWildcardManager


class DPGeneratorNode(ABC):
    RETURN_TYPES = ("STRING",)
    FUNCTION = "get_prompt"
    CATEGORY = "Dynamic Prompts"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "dynamicPrompts": False}),
                "seed": ("INT", {"default": 0, "display": "number"}),
            },
            "optional": {
                "wildcard_pipe": ("WILDCARD_PIPE",),
            },
        }

    def get_prompt(self, text: str, seed: int, wildcard_pipe = None) -> tuple[str]:
        if wildcard_pipe:
            wildcard_manager = PipeWildcardManager(wildcard_pipe)
        prompt = self.generate_prompt(text, seed, wildcard_manager)
        print(f"Prompt: {prompt}")

        return (prompt,)

    @abstractmethod
    def generate_prompt(self, text: str, seed: int, wildcard_manager) -> str:
        ...
