from scripts.Story_Runner import Story_Runner

def main():
    story_file = './story/start.json'
    runner = Story_Runner(story_file)
    runner.run_story()

main()