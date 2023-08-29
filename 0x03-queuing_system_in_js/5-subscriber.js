// Node Redis Client
import * as redis from 'redis';

const subscriber = redis.createClient();

// event handler for successful connection
subscriber.on('connect', () => {
    console.log('Redis client connected to the server');
});

// event handler for connection errors
subscriber.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`)
});

const CHANNEL = 'holberton school channel';

subscriber.subscribe(CHANNEL);

subscriber.on('message', (channel, message) => {
    if (channel === CHANNEL) console.log(message);

    if (message === 'KILL_SERVER') {
        subscriber.unsubscribe(CHANNEL);
        subscriber.quit();
    }
});
