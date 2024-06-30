#!/usr/bin/pup
# File: /path/to/your/manifests/install_flask.pp

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

