# NginxTornadoLoadBalancer

## Tornado Server

0. Write down code for service that displays the process pid for different input ports.
1. Run the service(python3 index.py 1111) using 3 different input ports (eg. 1111, 2222, 3333).
2. Go to localhost:1111/basic, localhost:2222/basic and localhost:3333/basic

## Nginx

0. sudo nginx (If it shows error then 1, else 2)
1. sudo fuser -k 80/tcp and service nginx start
2. Write down loadbalance.conf file for load balancing
3. Configure nginx.conf present in /etc/nginx/sites-available folder to use this loadbalance.conf file
4. Run this command to check the configration sudo nginx -t
5. Check the log file by going to sudo tail -f /var/log/nginx/access.log
6. Check by going to localhost/basic, it should route traffic on random sites
 
