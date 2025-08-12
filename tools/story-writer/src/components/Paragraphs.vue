<script setup lang="ts">
import { ref, Ref, computed } from "vue";
import storyJson from "../story_files/start.json";

defineProps({
  msg: String,
});

const isEditing = ref(false);

const paragraphArr = computed(() => {
  const storyNodeArr = [];
  for (const [nodeId, node] of Object.entries(storyJson).sort((a, b) => {
    console.log(a);
    console.log(b);
    return a[1].ui_location.paragraph - b[1].ui_location.paragraph;
  })) {
    node.id = nodeId;
    storyNodeArr.push(node);
  }
  return storyNodeArr;
});

function handleToggleEditMode() {
  isEditing.value = !isEditing.value;
}
</script>

<template>
  <div>
    <div class="header story-node">
      <div class="node-id-wrapper">
        <p class="node-id">Node ID</p>
      </div>
      <div class="lines">
        <div class="line">
          <p>Text / Options</p>
        </div>
      </div>
      <button class="edit-button" @click="handleToggleEditMode">
        {{ isEditing ? "Cancel" : "Edit" }}
      </button>
    </div>
    <div v-for="node of paragraphArr" :key="node.id" class="story-node">
      <div class="node-id-wrapper">
        <p class="node-id">{{ node.id }}</p>
      </div>
      <div class="lines">
        <div v-for="line of node.lines" class="line">
          <p class="line-text" v-if="!isEditing">{{ line.text }}</p>
          <textarea class="line-text" v-else v-model="line.text"></textarea>
        </div>
        <div
          v-if="!node.options || Object.keys(node.options).length === 0"
          class="option no-options-warning"
        >
          <span>This node is a dead end!</span> <button>Add options</button
          ><span> to fix this.</span>
        </div>
        <div
          v-else
          v-for="[optionText, nodeId] of Object.entries(node.options)"
          class="option"
        >
          <p>&bull; {{ optionText }} &lt;&lt;{{ nodeId }}&gt;&gt;</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
p {
  margin: 0;
}

.story-node {
  border: 1px solid #ccc;
  padding: 10px;
  margin: 10px;
  display: flex;
  align-items: center;
  margin: 0;
  padding: 0;
}

.story-node.header {
  background: lightskyblue;
  font-weight: bold;
}

.story-node.header > .lines {
  background: none;
}

.story-node.header > .node-id-wrapper {
  align-items: center;
}

.lines {
  display: flex;
  flex-direction: column;
  background: white;
  color: black;
  height: 100%;
  width: 90%;
}

.line {
  border-bottom: 0.5px dotted lightgray;
  margin: 0;
  padding: 5px;
  text-align: left;
  display: flex;
  width: 100%;
  justify-content: space-between;
}

.line-text {
  width: 100%;
  text-align: left;
  font-size: 16px;
  font-family: monospace;
  field-sizing: content;
  border: 0;
  background: none;
  box-sizing: content-box;
  line-height: 1.5;
  padding: 2px 5px;
  resize: none;
}

.toggle-edits {
  flex: 0;
}

.node-id-wrapper {
  height: -webkit-fill-available;
  width: 10%;
  display: flex;
  align-items: flex-start;
}

.node-id {
  width: 100%;
}

.option {
  width: 100%;
  display: flex;
  justify-content: left;
}

.no-options-warning {
  color: darkred;
  font-weight: bold;
  display: flex;
}
</style>
