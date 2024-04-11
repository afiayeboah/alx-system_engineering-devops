# A puppet manuscript to replace a line in a file on a server

$file_to_edit = '/var/www/html/wp-settings.php'

file_line { 'replace_phpp_with_php':
  path    => $file_to_edit,
  line    => 'php',
  match   => 'phpp',
  ensure  => present,
  replace => true,
}
