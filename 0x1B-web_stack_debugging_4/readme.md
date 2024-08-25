this is then 0x1B. Web stack debugging #4 project

web stack debugging task, 
tested how well our web server setup featuring Nginx is doing under pressure
it’s was not doing well: kept  getting a huge amount of failed requests.

For the benchmarking, was  using ApacheBench. It allows simulation of HTTP requests to a web server. In this case,
using the command ab -c 100 -n 2000 localhost/  I will make 2000 requests to my server with 100 requests at a time. 

We can see that 943 requests failed, let’s fix our stack so that we get to 0, and remember that when something is going wrong, logs are your best friends! 
