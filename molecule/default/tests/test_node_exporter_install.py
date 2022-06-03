
def test_node_exporter_package(host):
    package = host.package("node_exporter")
    assert package.is_installed

