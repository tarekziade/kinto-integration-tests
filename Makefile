build:
	virtualenv .
	bin/pip install -r dev-requirements.txt

test:
	bin/py.test --env=stage -v config-test/test_kinto_signer.py
