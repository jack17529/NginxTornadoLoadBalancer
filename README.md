# NginxTornadoLoadBalancer

Why use nginx to deploy tornado instead of its built-in server?

Since one Tornado process can only take advantage of one CPU core (Edit: See updated docs for a development on this), use Nginx to load-balance multiple Tornado processes to use multiple cores Additionally, Nginx is likely a more efficient static file handler than Tornado.

## Tornado Server

0. Write down code for service that displays the process pid for different input ports.
1. Run the service(python3 index.py 1111) using 3 different input ports (eg. 1111, 2222, 3333).
2. Go to localhost:1111/basic, localhost:2222/basic and localhost:3333/basic

## Nginx

Install nginx if not installed already.

0. sudo nginx (If it shows error then 1, else 2)
1. sudo fuser -k 80/tcp and service nginx start
2. Write down loadbalance.conf file for load balancing
3. Change default file present in /etc/nginx/sites-available folder to default file present in the repository
4. Run this command to check the configrations sudo nginx -s reload
5. Check the log file by going to sudo tail -f /var/log/nginx/access.log
6. Check by going to localhost/basic, it should route traffic on random sites based on round robin fashion.
7. Now stop one instance for example localhost:1111/basic by KeyboardInterrupt
8. The website at localhost/basic should redirect to only the remaining 2 instances
