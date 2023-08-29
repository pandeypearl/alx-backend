// Node Redis Client
import * as redis from 'redis';

const client = redis.createClient();

// event handler for successful connection
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

// event handler for connection errors
client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`)
});

// function to seta new school value in Redis
function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

// function to display the value for given school key
function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, res) => {
        console.log(res);
    });
}

// calling the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFranscisco', '100');
displaySchoolValue('HolbertonSanFranscisco');
