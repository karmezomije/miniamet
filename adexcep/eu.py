def is_network_in_sublist(network, sublist):
  """Checks if a network is in a sublist.

  Args:
    network: The network to check.
    sublist: The sublist to check in.

  Returns:
    True if the network is in the sublist, False otherwise.
  """

  for item in sublist:
    if network == item:
      return True

  return False
