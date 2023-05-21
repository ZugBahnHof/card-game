<script setup>
import {computed, ref} from 'vue'
import cards from "./cards.json"

/**
 * Shuffles array in place. ES6 version
 * @param {Array} a items An array containing the items.
 */
function shuffle(a) {
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

shuffle(cards);
shuffle(cards);
shuffle(cards);
shuffle(cards);
shuffle(cards);

defineProps({
  msg: String,
})

const time = ref(5000);

const cardChange = ref(false);

const upperZ = ref(0);
const lowerZ = ref(-1);


const count = ref(0);


const handleClick = () => {
  cardChange.value = true
  setTimeout(() => {
    cardChange.value = false
    upperZ.value = 0
    lowerZ.value = -1
  }, time.value)

  setTimeout(() => {
    upperZ.value = -5
    lowerZ.value = -4
  }, time.value / 20)

  setTimeout(() => {
    upperZ.value = -1
    lowerZ.value = 0
  }, time.value * 0.55)

  setTimeout(() => {
    upperZ.value = 0
    lowerZ.value = -1

    count.value = (count.value + 1) % cards.length;
    if (count.value === 0) {
      shuffle(cards);
      shuffle(cards);
      shuffle(cards);
      shuffle(cards);
      shuffle(cards);
    }
  }, time.value * 0.75)
}

// creat msTime as computed property
const msTime = computed(() => {
  return time.value + 'ms'
})

// create computed properties for the card values
const id = computed(() => {
  return cards[count.value].id
})
const name = computed(() => {
  return cards[count.value].name
})
const orange = computed(() => {
  return cards[count.value].action
})

const red = computed(() => {
  return cards[count.value].red
})
const green = computed(() => {
  return cards[count.value].green
})
const yellow = computed(() => {
  return cards[count.value].yellow
})
const blue = computed(() => {
  return cards[count.value].blue
})

</script>

<template>
  <div class="wrapper">
    <div class="card" :data-changing="cardChange" @click="handleClick">
      <div class="id" v-text="id"/>
      <div class="name" v-text="name"/>
      <div class="action" v-text="orange"/>
      <div class="red" v-text="red"/>
      <div class="green" v-text="green"/>
      <div class="yellow" v-text="yellow"/>
      <div class="blue" v-text="blue"/>
    </div>
    <div class="card card-back" :data-changing="cardChange"></div>
    <div class="card card-back card-stay"></div>
  </div>
</template>

<style scoped lang="scss">
.card {
  display: grid;
  gap: min(1em, 6vmin);
  background: whitesmoke;
  color: black;
  grid-template-areas:
  "id name name name"
  "action action action action"
  "red red green green"
  "yellow yellow blue blue";
  aspect-ratio: 59/92 !important;
  height: 75dvh;
  max-width: 80vw;
  place-items: center;
  padding: min(1em, 6vmin);
  border-radius: 1em;

  &[data-changing="true"] {
    animation: change;
    animation-duration: v-bind(msTime);
  }
}

@keyframes change {
  0% {
    transform: rotateY(0deg) translate3d(-0%, 0, 50%);
  }
  10% {
    transform: rotateY(90deg) translate3d(-75%, 0, 75%);
  }
  20% {
    transform: rotateY(180deg) translate3d(150%, 0, 0);
  }
  59.99999% {
    transform: rotateY(180deg) translate3d(0, 0, 0) scale(0.9);
  }
  60% {
    transform: rotateY(180deg) translate3d(0, 0, 0) scale(0.97);
  }
  100% {
    transform: rotateY(0deg) translate3d(0, 0, 0);
  }
}

.card div {
  padding: min(1em, 6vmin);
  border-radius: 1em;
  text-align: center;
  width: calc(100% - 2em);
  height: calc(100% - 2em);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: min(1em, 6vmin);
}

.id {
  grid-area: id;
  align-items: flex-start !important;
  justify-items: flex-start !important;
}

.name {
  grid-area: name;
  align-items: flex-start !important;
  justify-content: flex-end !important;
  text-align: right !important;
}

.action {
  grid-area: action;
  background: orange;
}

.red {
  grid-area: red;
  background: red;
}

.green {
  grid-area: green;
  background: green;
  color: white;
}

.yellow {
  grid-area: yellow;
  background: yellow;
}

.blue {
  grid-area: blue;
  background: blue;
  color: white;
}

.wrapper {
  // place both cards on top of each other
  position: relative;

  aspect-ratio: 59/92 !important;
  height: 75vh;

  & > .card {
    position: absolute;
    z-index: v-bind(upperZ);
    backface-visibility: hidden;
  }

  & > .card-back {
    z-index: v-bind(lowerZ);
    backface-visibility: visible;
  }

  & > .card-stay {
    z-index: -3 !important;
    transform: rotateY(180deg) scale(0.97);
    backface-visibility: visible;
  }
}

.card-back {
  background: repeating-conic-gradient(
          from 0deg,
          #fff 0deg 90deg,
          #000 0deg 180deg);
}

</style>
