# Adjust the OS configuration to enable seamless login with 
# the holberton user and file opening without encountering any error messages

exec {'OS security config':
  command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',
  path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/'
}
