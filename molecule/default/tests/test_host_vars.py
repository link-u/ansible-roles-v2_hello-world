import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_check_host_vars(host):
    ansible_vars = host.ansible.get_variables()
    assert ansible_vars["test_username"] == "alice"
    assert ansible_vars["test_password"] == "hogehoge"
    assert True
