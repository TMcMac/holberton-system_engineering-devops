# Install nginx listening on port 80, static html = Holberton School, perm redirect 301

package { 'nginx':
  ensure => 'installed',
  package_source => 'nginx-mainline'
}

file { 'index.html':
  path => '/var/www/html/index.html',
  ensure  => present,
  content => 'Holberton School'
}

file { 'custom_404.html':
  path => '/var/www/html/custom_404.html',
  ensure  => present,
  content => 'Ceci n'est pas une page'
}

exec { 'sed1':
  path => '/usr/bin/env:/usr/bin:/usr/sbin:/bin',
  command => 'sed -i "/^[[:blank:]]*server_name/s/$/\n\trewrite ^\/redirect_me https:\/\/www.youtube.com\/watch?v=dQw4w9WgXcQ permanent;/" /etc/nginx/sites-available/default'
}
