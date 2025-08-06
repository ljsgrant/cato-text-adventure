<script setup lang="ts">
import { ref, Ref, computed } from "vue";
import storyJson from "../story_files/start.json";

defineProps({
  msg: String,
});

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
</script>

<template>
  <div>
    <div v-for="node of paragraphArr" :key="node.id" class="story-node">
      <div class="node-id-wrapper">
        <p class="node-id">{{ node.id }}</p>
      </div>
      <div class="lines">
        <div v-for="line of node.lines" class="line">
          <p>{{ line.text }}</p>
        </div>
        <div
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
</style>
