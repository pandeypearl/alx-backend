# 0x03. Queuing System in JS

This project covers the following concepts: 

+ How to run a Redis server on your machine
+ How to run simple operations with the Redis client
+ How to use a Redis client with Node JS for basic operations
+ How to store hash values in Redis
+ How to deal with async operations with Redis
+ How to use Kue as a queue system
+ How to build a basic Express app interacting with a Redis server
+ How to the build a basic Express app interacting with a Redis server and queue

| file | Description |
| --- |:--- |
| [0-redis_client.js](0-redis_client.js) |  Connects to the Redis server |
| [1-redis_op.js](1-redis_op.js) | Contains setNewSchool, displaySchoolValue |
| [2-redis_op_async.js](2-redis_op_async.js) | Uses promisify to modify displaySchoolValue |
| [4-redis_advanced_op.js](4-redis_advanced_op.js) | Using the client to store a hash value |
| [5-subscriber.js](5-subscriber.js) | Creates redis client subscriber |
| [5-publisher.js](5-publisher.js) | Create redis client publisher | 
| [6-job_creator.js](6-job_creator.js) | Creates the job creator | 
| [6-job_processor.js](6-job_processor.js) | Create the job processor | 
| [7-job_creator.js](7-job_creator.js) | Tracks progress and errors with Kue: Create the Job creator  |
| [7-job_processor.js](7-job_processor.js) | Track progress and errors with Kue: Create the Job processor |
| [8-job.js](8-job.js) | Job creation function | 
| [8-job-main.js](8-job-main.js) | Testing code for 8-job.js |
| [8-job.test.js](8-job.test.js) | Unit Tests for job creation |
| [9-stock.js](9-stock.js) | Script to check product stock | 
| [100-seat.js](100-seat.js) | Script to check available seats | 

To run files (with .js extension): 
<pre><code>
npm run dev filename
</code></pre>

To run test files (with .test.js extention):
<pre><code>
npm test filename 
</code></pre>

For 9-stock.js:
<pre></code>
curl localhost:1245/list_products/1 ; echo ""
</code></pre>
<pre></code>
curl localhost:1245/list_products/12; echo ""
</code></pre>
<pre></code>
curl localhost:1245/reserve_product/12 ; echo ""
</code></pre>
<pre></code>
curl localhost:1245/reserve_product/1 ; echo ""
</code></pre>
<pre></code>
curl localhost:1245/reserve_product/1 ; echo ""
</code></pre>

for 100-seat.js:
<pre><code>
curl localhost:1245/available_seats ; echo ""
</code></pre>
<pre><code>
curl localhost:1245/reserve_seat ; echo ""
</code></pre>
<pre><code>
curl localhost:1245/process ; echo ""
</code></pre>
<pre><code>
curl localhost:1245/available_seats ; echo ""
</code></pre>
<pre><code>
Seat reservation job 52 completed
for n in {1..50}; do curl localhost:1245/reserve_seat ; echo ""; done
</code></pre>