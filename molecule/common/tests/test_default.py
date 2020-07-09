import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_hello_dest_path(host):
    ansible_vars = host.ansible.get_variables()
    filepath = ansible_vars["hello_dest_path"]
    assert host.file(filepath).exists
    assert not host.ansible(
        "copy",
        "content=\"Hello, ansible!\" " \
        "dest=\"{{ hello_dest_path }}\"")["changed"]


## hosts.ansible() を使って色々実験した痕跡
# def test_ansible_variables(host):
#     print(host.ansible.get_variables())
#     #defaults_files = "file=../../defaults/main.yml name=role_defaults"
#     #print(host.ansible("include_vars", defaults_files))
#     #print(host.ansible("include_vars", defaults_files)["ansible_facts"]["role_defaults"])
#     #print(get_vars(host))
#     #print(get_vars(host)["hello_dest_path"])
#     assert True

# def get_vars(host):
#     defaults_files = "file=../../defaults/main.yml name=role_defaults"
#     ansible_vars = host.ansible(
#         "include_vars",
#         defaults_files)["ansible_facts"]["role_defaults"]
#     return ansible_vars
