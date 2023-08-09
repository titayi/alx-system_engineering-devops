# A puppet manuscript to replace rewrite a line

$file_path = '/var/www/html/wp-settings.php'

# Replacing 'phpp' with 'php'

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_path}",
  path    => ['/bin','/usr/bin']
}
