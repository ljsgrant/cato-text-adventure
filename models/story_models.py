from typing import Dict
from pydantic import BaseModel, model_validator, RootModel
from enum import Enum

class UI_Location(BaseModel):
    """
    A location for a node in the UI
    """
    x: int
    y: int

class CheckTarget(Enum):
    """
    Valid bits of state for checks
    """
    inventory = "inventory"
    interactions = "interactions"
    characters = "characters"
    current_location = "current_location"

class CheckLogic(Enum):
    """
    Valid types of checks
    """
    all = "all"
    any = "any"

class Check(BaseModel):
    """
    A check against current state that can be used to conditionally show text on a node
    """
    target: CheckTarget
    check: bool
    content: str

class Condition(BaseModel):
    """
    A condition contains a series of checks against state and 
    can be used to conditionally show text on a node
    """
    type: CheckLogic
    checks: list[Check]

class Line(BaseModel):
    """
    A line of text that can be conditionally shown on a node
    """
    condition: Condition | None = None
    text: str

class StoryNode(BaseModel):
    """
    A node in the story
    """
    ui_location: UI_Location | None = None
    lines: list[Line]
    options: dict[str, str]

class Story(RootModel[Dict[str, StoryNode]]):
    @model_validator(mode="after")
    def validate_all_option_targets_exist(self):
        all_nodes = set(self.root.keys())
        for node_id, node in self.root.items():
            if node_id == "exit":
                continue
            for option_label, target in node.options.items():
                if target not in all_nodes:
                    raise ValueError(
                        f"Node '{node_id}' has an option '{option_label}' "
                        f"pointing to unknown node '{target}'"
                    )
        return self

    





    