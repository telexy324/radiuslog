# Pull base image  
FROM centos:7.4.1708 
  
MAINTAINER yang xu "gis324@sina.com"  
  
# Install Environment
RUN yum -y install epel-release
RUN yum -y install openssh-clients wget vixie-cron ntpdate
RUN yum -y install git python-pip
RUN pip install --upgrade pip

# Install Gunicorn
RUN pip install gunicorn
  
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
