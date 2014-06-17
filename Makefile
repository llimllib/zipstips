deploy:
	rsync -avuz . llimllib@hubvan.com:/srv/zipstips/
	ssh llimllib@hubvan.com touch /srv/slask/wsgi.py
