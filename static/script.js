var degree = 180;
const timeout = 200;

window.onload = function updateImage() {
    document.getElementById("whiteboard").src = "/static/result.png#t=" + new Date().getTime();
    setTimeout(updateImage, timeout);
}

function rot180() {
    document.getElementById("whiteboard").style.transform = "rotate(" + degree + "deg)";
    degree += 180;
}

function updateImage() {
    document.getElementById("whiteboard").src = "/static/result.png#t=" + new Date().getTime();
    setTimeout(updateImage, timeout);
}

const userAction = async () => {
    const response = await fetch("/hostname");
    const json = await response.json();
    window.alert("Your hostname is: " + json.hostname + "\nYour port is: " + json.port);
}