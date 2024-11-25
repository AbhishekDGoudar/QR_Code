css = """

"""


index = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Full-Page Flip Animation</title>
    <style>
        body {
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: Arial, sans-serif;
            perspective: 1000px;
            margin: 0;
            background-color: #e0e0e0;
        }

        .flip-container {
            width: 800px; /* Fixed width */
            height: 900px; /* Fixed height */
            position: relative;
            transform-style: preserve-3d;
            transition: transform 1s ease-in-out;
        }

        .flip-container.flipped {
            transform: rotateY(180deg);
        }

        .front, .back {
            width: 100%;
            height: 100%;
            position: absolute;
            backface-visibility: hidden;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            font-size: 1.5rem;
            font-weight: bold;
            text-align: center;
            border: 2px solid #ccc;
            border-radius: 15px;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .front {
            color: #000;
        }

        .back {
            color: #000;
            transform: rotateY(180deg);
        }

        img {
            max-width: 100%;
            max-height: 70%;
            margin-top: 20px;
            border: 2px solid #000;
            border-radius: 10px;
            object-fit: contain;
        }


        .grid-container {
            display: grid;
            grid-template-columns: repeat(2, 1fr); /* 2 columns */
            grid-gap: 20px;
            width: 80%;
            max-width: 800px;
        }

        .grid-item {
            background-color: white;
            padding: 10px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            text-align: center;
            border: 1px solid #ddd;
        }

        .grid-item iframe {
            width: 100%;
            height: 200px;
            border: none;
            border-radius: 8px;
            margin-bottom: 10px;
        }

        .grid-item button {
            padding: 8px 16px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 1rem;
        }

        .grid-item button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="flip-container" id="flipContainer">
        <div class="front">
            <h1>CTRL + ALT + MEME</h1>
            <img id="randomImage" alt="Meme">
        </div>
        <div class="back">
            <h1>I know you weren't here for Memes. Here's the content you are looking for</h1>
            <div class="grid-container" id="gridContainer"></div>

        </div>
    </div>

    <script>
        // Variable to control the size of the grid (2 x 2 grid)
        let m = 1; // Number of rows
        let n = 2; // Number of columns


        const gridContainer = document.getElementById('gridContainer');

        // Example embedded HTML preview URLs (could be YouTube videos, websites, etc.)
        const embeds = [
            "https://mavsuta-my.sharepoint.com/:u:/g/personal/txk4530_mavs_uta_edu/EbnaVh-VbwNEsqbXORImvKkBwvAoshMQYHpK0qOtJWAahw?email=adg6610%40mavs.uta.edu&e=slLnGb", // YouTube video
            "https://github.com/AbhishekDGoudar/Job-Skills-Recommendations/", // W3Schools HTML Editor
        ];

        function createGrid() {
            gridContainer.innerHTML = ''; // Clear the grid before re-building

            // Set grid layout dynamically based on m (rows) and n (columns)
            gridContainer.style.setProperty('grid-template-columns', `repeat(${n}, 1fr)`);

            // Create the grid items based on m and n
            for (let i = 0; i < m * n; i++) {
                const gridItem = document.createElement('div');
                gridItem.classList.add('grid-item');

                // Create iframe for HTML preview
                const iframe = document.createElement('iframe');
                iframe.src = embeds[i % embeds.length]; // Use embeds cyclically
                iframe.title = `Embed ${i + 1}`;

                // Button with clickable text
                const button = document.createElement('button');
                button.textContent = `Link`;
                button.onclick = () => {
                    window.open(embeds[i % embeds.length], '_blank'); // Opens the URL in a new tab
                };

                // Append iframe and button to the grid item
                gridItem.appendChild(iframe);
                gridItem.appendChild(button);

                // Add the grid item to the container
                gridContainer.appendChild(gridItem);
            }
        }

        // Create the grid on page load
        createGrid();
    </script>
    <script>
        // Flip the page every 15 seconds
        function autoFlip() {
            const flipContainer = document.getElementById('flipContainer');
            setInterval(() => {
                flipContainer.classList.toggle('flipped');
            }, 15000);
        }

        // Initialize the auto-flip
        autoFlip();

        const images = [
            "meme_1.png",
            "meme_2.png",
            "meme_3.png",
            "meme_4.png",
            "meme_5.png",
            "meme_6.png",
            "meme_7.png",
            "meme_8.png",
            "meme_10.png",
            "meme_11.png",
            "meme_12.png",
            "meme_13.png",
            "meme_14.png",
            "meme_15.png"
        ];

        // Function to select a random image
        function getRandomImage() {
            const randomIndex = Math.floor(Math.random() * images.length);
            return images[randomIndex];
        }

        // Set the src attribute of the image element
        const imgElement = document.getElementById('randomImage');
        imgElement.src = getRandomImage();
    </script>
</body>
</html>

"""