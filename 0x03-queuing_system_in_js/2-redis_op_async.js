// Node Redis Client
import * as redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

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
async function displaySchoolValue(schoolName) {
    const value = await getAsync(schoolName);
    console.log(value);
}

// calling the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFranscisco', '100');
displaySchoolValue('HolbertonSanFranscisco');
