class DPWildcardPipe:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "name": ("STRING", {"default": ""}),
                "text": ("STRING", {"multiline": True, "dynamicPrompts": False}),
                "delimiter": (["Space", "Comma", "Pipe", "Newline"], {"default": "Comma"}),
            },
            "optional": {
                "wildcard_pipe": ("WILDCARD_PIPE",),
            },
        }

    RETURN_TYPES = ("WILDCARD_PIPE",)
    RETURN_NAMES = ("wildcard_pipe",)
    FUNCTION = "add_to_pipe"
    CATEGORY = "Dynamic Prompts"

    def __init__(self) -> None:
        self._delimiter_dict = {
            "Space": " ",
            "Comma": ",",
            "Pipe": "|",
            "Newline": "\n",
        }

    def add_to_pipe(self, name, text, delimiter, wildcard_pipe = None) -> tuple[dict[str, list[str]]]:
        if name and text:
            delimiter = self._delimiter_dict[delimiter]
            values = [x.strip() for x in text.strip().split(delimiter)]
            return ((wildcard_pipe or {}) | {name: values},)
        else:
            return (wildcard_pipe,)
        
class PipeWildcardManager:
    def __init__(self, wildcard_dict):
        self.wildcard_dict = wildcard_dict

    def get_all_values(self, wildcard: str) -> list[str]:
        if wildcard in self.wildcard_dict:
            return self.wildcard_dict[wildcard]
        else:
            return [wildcard]