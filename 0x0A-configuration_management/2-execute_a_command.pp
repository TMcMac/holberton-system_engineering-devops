# Puppet command execute to kill a specific process

exec { 'pkill':
  path    => '/usr/bin:/usr/sbin:/bin',
  command => 'pkill -f killmenow'
}