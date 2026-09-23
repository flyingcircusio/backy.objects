# backy.objects

backy.objects is a tool for backing up Ceph-based S3-compatible object storages (RadosGW, rgw) using the
[bucket notifications](https://docs.ceph.com/en/latest/radosgw/notifications/) feature.

It is inspired by [backy](https://github.com/flyingcircus/backy) and intended to complement it.

It enables:

* continuous near real-time syncing
* syncing object and meta data
* monitoring

It is inspired by [backy]


## Competing solutions


* rclone is too slow, resource intensive, coarse grained and it's ability to store on the filesystem is limited and can lead to errors mapping keys with conflicting or long names

* zone replication is too coarse grained


## Unsupported / untested features

* [ ] object versioning


## MVP TODO

### source side

- [ ] provide a local endpoint, explicitly bound to an IP, that is configured (and updated?) in the rgw as the receiver for events

- [ ] forward to the remote endpoint via https that carries basically 1:1 of the event data

- [ ] ensure proper signalling for ceph whether an event was received - do we want to decouple this and signal ceph once we received an event and then keep our own queue or do we want to wait on the remote side

- [ ] compression (is https compression sufficient?)

### target side

 * [ ] ensure correct ownership (likely needs username mapping), manage credentials

 * [ ] replicate into local rgw

 * [ ] replicate into local storage (/srv/backy.objects/<user>/), use content hashing for objects and keep track of path to object content hashing and metadata in a sqlite database

 * [ ]     (do we need to deal with multi-part or can we just defer on multi-part?)

* [ ] authentication (shared secret sufficient for now?)


Architecture and Design Goals
==============================

backy.objects consists of two daemons that facilitate sending messages from one source Ceph cluster to a destination location over HTTPs.

* A daemon that runs in the source Ceph cluster that is the target of the local bucket notifications

* A daemon on the target Ceph cluster and Backup server that sends the incoming data both to the Ceph cluster and the local disk

* Visibility: prometheus output and local interactions

* Monitoring: status per user and bucket?

* Operability: ???

* Configuration: single instance of the daemon on each side that can automatically pick up the buckets to sync

* We leverage asyncio consistently.

* We keep it simple KISS and avoid flurries of dependecies. Ask before adding new dependencies and argue why they are needed.

Implementation Guidance
=======================


* Use `pytest` for everything, pay attention to coverage
* Use scriv to record
* Use branches for each feature
* Use pydantic for json serialization/deserialization
* Use type annotations consistently. Avoid `Any`.
* Do not stage changes yourself. Draft a commit message and show it, then let me stage the changes and I'll ask you to commit.
* You never push, only human operators do.

Roadmap / Later
===============

* [ ] Snapshots and cleanup

* [ ] ....
