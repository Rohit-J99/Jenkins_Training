package policy1

allow[msg] {
	input.val == "true"
	msg = "working"
}