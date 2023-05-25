package policy1

test_pass {
	allow with input as {"val": true}
}

test_fail {
	allow with input as {"val": false}
}