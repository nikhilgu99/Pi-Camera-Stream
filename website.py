WEBPAGE="""\
<html>

<head>
	<title>Nikhil's Pi Stream</title>
	<script tpye="text/javascript" src="https://github.com/niklasvh/html2canvas/releases/download/v1.0.0-rc.5/html2canvas.js"></script>
	<style>
		
	body {
		background-color: #9f9f9f;
	}

	#feed {
		border: 2px solid purple;
		height: 80vh;
		margin-left: 10vw;
		width: 80vw;
	}
	
	#picButton{
		background-color: #4CAF50;
		color: white;
		margin-bottom: 5px;	
		margin-left: 45%;
		margin-top: 5px;
		padding: 10px 21px;
		width: 10%;
	}
	
	#screenshotDiv{
		background-color: #9f9f9f;
		margin: 5px 0px 5px 0px;
	}

	#title{
		color: orange;
		font-family: Arial, Helvetica, sans-serif;
		font-size: 24px;
		margin-bottom: 0px;
		text-align: center;
		text-decoration: underline;
	}
	</style>
	
	<script>
		function takePic(){
			html2canvas(document.getElementById("screenshotDiv")).then(function(canvas) {
    		document.body.appendChild(canvas);
    		//var image = canvas.toDataURL("image/png").replace("image/png", "image/octet-stream");
    		//window.location.href=image;  		
   		});		
		}
	</script>
</head>

<body>
	<h1 id="title">Live Feed</h1>
	<button id="picButton" type="button" onclick="takePic()">Take a Picture!</button>
	<div id="screenshotDiv">
		<img id="feed" src="stream.mjpg">
	</div>
</body>

</html>
"""