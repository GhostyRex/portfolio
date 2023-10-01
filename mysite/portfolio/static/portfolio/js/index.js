text = document.getElementById('i-am-python');

console.log(text.style.color);
text.style.opacity = "0.6";

changeColor = () => {
    if (text.style.opacity == "1") {
      text.style.opacity = "0.6";
    } else {
      text.style.opacity = "1";
    }
  }

setInterval(changeColor, 2500);
