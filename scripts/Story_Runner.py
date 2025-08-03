import json

class Story_Runner:
    def __init__(self, story_file):
        self.story_file = story_file
        self.story = self.load_story(story_file)
        self.run_story()

    def load_story(self, file_path):
        with open(file_path, 'r') as file:
            story = file.read()
            story_json = json.loads(story)
        return story_json

    def run_story(self):
        start_node = self.story["start"]
        self.run_node(start_node)

    def run_node(self, node):
        for line in node["lines"]:
            print(line["text"])
            input("")
        if "options" in node and len(node["options"]):
            print("Options:")
            for text in node["options"].keys():
                print(text)
            user_input = ""
            while not node["options"].get(user_input):
                user_input = input("You: ")
                
            next_node_id = node["options"].get(user_input)
            next_node = self.story[next_node_id]
            self.run_node(next_node)