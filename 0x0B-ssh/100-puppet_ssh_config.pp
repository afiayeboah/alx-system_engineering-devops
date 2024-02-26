# Define SSH client configuration
class ssh_config {
    # Set SSH client to use private key ~/.ssh/school
    file_line { 'Declare identity file':
        path               => '/etc/ssh/ssh_config',
        line               => '    IdentityFile ~/.ssh/school',
        match              => '^[\s]*IdentityFile[\s]+~/.ssh/id_rsa$',
        replace            => true,
        append_on_no_match => true,
    }

    # Disable password authentication
    file_line { 'Turn off passwd auth':
        path               => '/etc/ssh/ssh/config',
        line               => '    PasswordAuthentication no',
        match              => '^[\s]*PasswordAuthentication[\s]+(yes|no)$',
        replace            => true,
        append_on_no_match => true,
    }
}

# Apply SSH client configuration
include ssh_config

