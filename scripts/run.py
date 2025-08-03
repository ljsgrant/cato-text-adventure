import Story_Runner as Runner

def main():
    story_file = '../story/start.json'
    runner = Runner.Story_Runner(story_file)
    runner.run_story()

main()