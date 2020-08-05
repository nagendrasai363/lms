// 2. This code loads the IFrame Player API code asynchronously.
var tag = document.createElement('script');

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

// 3. This function creates an <iframe> (and YouTube player)
//    after the API code downloads.
var playerDivs = document.querySelectorAll(".player"); // get .player nodes
var playerDivsArr = [].slice.call(playerDivs); // nodelist to array to use forEach();
var players = new Array(playerDivsArr.length);

// when youtube stuff is ready
function onYouTubeIframeAPIReady() {
  
  // create yt players
  playerDivsArr.forEach(function(e, i) { // forEach ...
    players[i] = new YT.Player(e.id, {
      videoId: e.id,
      width:"100%",
      height:"562",
      events: {
            'onReady': onPlayerReady,
            'onStateChange': onPlayerStateChange
          }
    })
  })

  
}
function onPlayerReady(event) {
    //
  }
function changeBorderColor(playerStatus) {
    var color;
    if (playerStatus == -1) {
      color = "#37474F"; // unstarted = gray
    } else if (playerStatus == 0) {
      color = "#FFFF00"; // ended = yellow
      alert('im ended')
    } else if (playerStatus == 1) {
      color = "#33691E"; // playing = green
    } else if (playerStatus == 2) {
      color = "#DD2C00"; // paused = red
      //alert('im paused')
    } else if (playerStatus == 3) {
      color = "#AA00FF"; // buffering = purple
    } else if (playerStatus == 5) {
      color = "#FF6DOO"; // video cued = orange
    }
    if (color) {
      document.getElementById('existing-iframe-example').style.borderColor = color;
    }
  }
function onPlayerStateChange(event) {
    changeBorderColor(event.data);
  }








