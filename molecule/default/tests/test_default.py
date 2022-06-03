import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

@pytest.mark.parametrize('pkg', [
  'node_exporter'
])

def test_pkg(host, pkg):
    package = host.package(pkg)

    assert package.is_installed

def test_svc(host):
   service = host.service("node_exporter")
   assert service.is_running
   assert service.is_enabled

# @pytest.mark.parametrize('file, content', [
#   ("/etc/firewalld/zones/public.xml", "<service name=\"http\"/>"),
#   ("/var/www/html/index.html", "Managed by Ansible")
# ])
# def test_files(host, file, content):
#     file = host.file(file)

#     assert file.exists
#     assert file.contains(content)