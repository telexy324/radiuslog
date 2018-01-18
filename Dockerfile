# Pull base image  
FROM 192.168.30.46:5000/xuyang/centos7.4
  
MAINTAINER yang xu "gis324@sina.com"  
 
# Add code from local
RUN mkdir -p /opt/radiuslog
COPY app /opt/radiuslog/app
COPY tests /opt/radiuslog/tests
COPY config.py manage.py requirements.txt /opt/radiuslog/

# Install Requirement
RUN pip install -r /opt/radiuslog/requirements.txt
  
# Crontab
# RUN echo "* * * * * ntpdate 192.168.1.250" >> /var/spool/cron/root

# Expose ports.  
EXPOSE 5000

ENTRYPOINT cd /opt/radiuslog && gunicorn --workers=3 -b 0.0.0.0:5000 manage:app
