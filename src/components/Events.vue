<template>
  <h1>Events</h1>
  <p>Warning: Don't refresh or close this page</p>
  <p>Your color:
    <span class="color-preview">{{ color }}</span>
  </p>
  <p>
    <button
        type="button"
        @click="handleClick"
    >
      Get new event!
    </button>
  </p>
  <div v-html="eventText"></div>
</template>

<script>
const colors = ["red", "green", "yellow", "blue"];

function getRandomNumber(min, max) {
  // Get the range of numbers (max - min + 1) and create a typed array to hold it
  const range = max - min + 1;
  const array = new Uint32Array(1);

  // Generate random values until we get a number within the desired range
  let randomNumber;
  do {
    crypto.getRandomValues(array);
    randomNumber = array[0] % range;
  } while (randomNumber >= range);

  // Add the random number to the minimum value to get a number within the desired range
  return min + randomNumber;
}


export default {
  name: "Events",
  mounted() {
  },
  data() {
    return {
      color: "orange",
      eventText: "",
    }
  },
  computed: {
    fontColor() {
      return ["blue", "green"].includes(this.color) ? "white" : "black";
    }
  },
  methods: {
    handleClick() {
      this.eventText = "...";

      setTimeout(() => {
            let pick = getRandomNumber(0, 110);

            if (pick > 80) {
              let c = getRandomNumber(0, 3);
              this.color = colors[c];

              this.eventText = `Set color to <span class='color-preview'>${this.color}</span>`;
            } else if (pick > 70) {
              this.eventText = "You can see the number of points of someone";
            } else if (pick > 60) {
              this.eventText = "You have to swap points with someone";
            } else if (pick > 57) {
              this.eventText = "Everyone gives you 10 points";
            } else if (pick > 54) {
              this.eventText = "You have to tell your color publicly";
            } else if (pick > 50) {
              this.eventText = "Multiply your points by 1.2 (round to zero)";
            } else if (pick > 46) {
              this.eventText = "Multiply your points by 0.8 (round to zero)";
            } else {
              this.eventText = "Nothing happens ..."
            }

          },
          100
      )
    }
  },
}
</script>

<style scoped>
.color-preview {
  background: v-bind(color);
  color: v-bind(fontColor);
  padding: 0.25em;
  border-radius: 0.25em;
  margin-left: 0.5em;
}

div {
  aspect-ratio: 2;
  width: 100%;
  flex-grow: 1;
  border: 1px solid #666;
  border-radius: 0.5em;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5em;
}
</style>
