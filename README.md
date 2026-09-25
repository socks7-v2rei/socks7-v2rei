<div align="center">
  <img src="assets/hero.svg" width="100%" alt="SOCKS7 — Next Generation Encrypted Proxy Protocol"/>
</div>

<div align="center">
  <strong>EN</strong> &nbsp;·&nbsp; <a href="README.fa.md">فارسی</a>
</div>

<br/>

<div align="center">

> **SOCKS7** is not "another proxy". It is a ground-up transport fabric that carries *many* logical streams over a *single* obfuscated socket — with a 2-RTT zero-knowledge handshake, forward secrecy, and automatic least-latency egress failover.

</div>

<br/>

## ⚡ See it move

<div align="center">
  <img src="assets/terminal.svg" width="92%" alt="socks7 live terminal session"/>
</div>

<br/>

## 🧬 Why SOCKS7 exists

|  | Classic SOCKS5 | **SOCKS7** |
|---|---|---|
| Streams per connection | 1 | **unlimited (multiplexed)** |
| Handshake | plaintext negotiation | **2-RTT zero-knowledge** |
| Key exchange | none | **ephemeral X25519 + PSK** |
| Cipher suite | none / external | **XChaCha20-Poly1305** |
| UDP | awkward | **native, first-class** |
| Failover | manual | **automatic, least-latency** |
| Fingerprint | obvious | **obfuscated (TLS 1.3 cover)** |

<br/>

<div align="center">
  <img src="assets/topology.svg" width="100%" alt="SOCKS7 multiplexed tunnel topology"/>
</div>

<br/>

## 🔐 The handshake

<div align="center">
  <img src="assets/handshake.svg" width="100%" alt="SOCKS7 handshake sequence"/>
</div>

<br/>

## 📡 Live telemetry

<div align="center">
  <img src="assets/metrics.svg" width="100%" alt="SOCKS7 live telemetry dashboard"/>
</div>

<br/>

## 🌐 The fabric

<div align="center">
  <img src="assets/contribution-network.svg" width="100%" alt="SOCKS7 contribution network"/>
</div>

<br/>

## 🧰 Quick start

```bash
# 1 · install
curl -fsSL https://socks7.dev/install.sh | sh

# 2 · spin up a local edge node
socks7 node --listen :1080 --cipher xchacha20 --obfs tls1.3

# 3 · route any client through the fabric
socks7 connect --peer edge-1.eu --streams 4
```

```python
from socks7 import Client

with Client("127.0.0.1:1080", streams=8) as c:
    for host in ("api.example.com", "cdn.example.com"):
        c.get(f"https://{host}/")   # multiplexed over one socket
```

<br/>

## 🗺 Roadmap

```text
[x]  v7.0  core transport · mux · XChaCha20            <- shipping
[ ]  v7.1  QUIC datagram mode · 0-RTT resume
[ ]  v7.2  pluggable transports marketplace
[ ]  v7.3  hardware offload + kernel bypass (io_uring)
[ ]  v8.0  post-quantum hybrid KEM (X25519 + Kyber)
```

<br/>

## 🔗 Connect

<div align="center">
  <img src="assets/badges.svg" width="720" alt="SOCKS7 badges"/>
</div>

<div align="center">

[**socks7.dev**](#) &nbsp;·&nbsp; [**Docs**](#) &nbsp;·&nbsp; [**Releases**](#) &nbsp;·&nbsp; [**Discussions**](#)

</div>

<div align="center">
  <sub><code>// built one packet at a time · SOCKS7 © 2026</code></sub>
</div>
