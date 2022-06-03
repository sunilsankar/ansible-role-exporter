def test_node_exporter_service(host):
   service = host.service("node_exporter")
   assert service.is_running
   assert service.is_enabled

