#!/usr/bin/pup
# flask is installed in a specific version

package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
