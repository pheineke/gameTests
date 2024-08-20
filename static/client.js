const canvas = document.getElementById('gameCanvas');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const ctx = canvas.getContext('2d');
const socket = io();

const WORLD_WIDTH = 2000; // Breite der Welt
const WORLD_HEIGHT = 2000; // Höhe der Welt
const VIEWPORT_WIDTH = canvas.width;
const VIEWPORT_HEIGHT = canvas.height;

let arr = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'brown', 'black', 'white'];
let bushes = []; // Die Büsche, die vom Server empfangen werden

/* Server Actions Controller */
socket.on('update_positions', (players) => {
    ctx.clearRect(0, 0, VIEWPORT_WIDTH, VIEWPORT_HEIGHT);
    // Zuerst die Büsche zeichnen
    drawBushes();

    // Dann die Spieler zeichnen
    for (let id in players) {
        const pos = players[id];
        ctx.fillStyle = id === playerId ? 'blue' : 'red';
        ctx.fillRect(pos.x - camera.x, pos.y - camera.y, 5, 5);
    }
});

socket.on('init_bushes', (serverBushes) => {
    bushes = serverBushes;
});

function drawBushes() {
    ctx.fillStyle = 'green';
    bushes.forEach(bush => {
        ctx.fillRect(bush.x - camera.x, bush.y - camera.y, bush.size, bush.size);
    });
}

function checkCollision(newX, newY) {
    // Check if the player's new position collides with any bush
    for (let bush of bushes) {
        if (newX < bush.x + 30 && newX + player.width > bush.x &&
            newY < bush.y + 30 && newY + player.height > bush.y) {
            return true; // Kollision entdeckt
        }
    }
    return false; // Keine Kollision
}

function createPlayer() {
    let player = {
        id: Math.random().toString(36).substring(2, 9),
        x: Math.random() * WORLD_WIDTH,
        y: Math.random() * WORLD_HEIGHT,
        height: 10,
        width: 10,
        speed: 5,
        color: arr[Math.floor(Math.random() * arr.length)]
    };
    return player;
}

function movePlayer(event) {
    switch (event.key) {
        case 'ArrowUp':
            player.y -= player.speed;
            break;
        case 'ArrowDown':
            player.y += player.speed;
            break;
        case 'ArrowLeft':
            player.x -= player.speed;
            break;
        case 'ArrowRight':
            player.x += player.speed;
            break;
    }

    // Update player position
    socket.emit('player_move', { id: playerId, position: player });

    // Update camera position
    camera.x = player.x - VIEWPORT_WIDTH / 2;
    camera.y = player.y - VIEWPORT_HEIGHT / 2;

    // Keep the camera within the world bounds
    camera.x = Math.max(0, Math.min(camera.x, WORLD_WIDTH - VIEWPORT_WIDTH));
    camera.y = Math.max(0, Math.min(camera.y, WORLD_HEIGHT - VIEWPORT_HEIGHT));
}

let camera = { x: 0, y: 0 }; // Kamera-Position






function init() {
    player = createPlayer();
    playerId = player.id;
    socket.emit('player_join', player);
}

document.addEventListener('DOMContentLoaded', function () {
    init();
    window.addEventListener('keydown', movePlayer);
});

