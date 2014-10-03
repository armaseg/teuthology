import docopt

import teuthology.suite

doc = """
usage: teuthology-suite --help
       teuthology-suite --suite <suite> [options] [<config_yaml>...]

Run a suite of ceph integration tests. A suite is a directory containing
facets. A facet is a directory containing config snippets. Running a suite
means running teuthology for every configuration combination generated by
taking one config snippet from each facet. Any config files passed on the
command line will be used for every combination, and will override anything in
the suite. By specifying a subdirectory in the suite argument, it is possible
to limit the run to a specific facet. For instance -s upgrade/dumpling-x only
runs the dumpling-x facet of the upgrade suite.

Miscellaneous arguments:
  -h, --help                  Show this help message and exit
  -v, --verbose               Be more verbose
  --dry-run                   Do a dry run; do not schedule anything

Standard arguments:
  <config_yaml>               Optional extra job yaml to include
  -s <suite>, --suite <suite>
                              The suite to schedule
  -c <ceph>, --ceph <ceph>    The ceph branch to run against
                              [default: master]
  -k <kernel>, --kernel <kernel>
                              The kernel branch to run against
                              [default: testing]
  -f <flavor>, --flavor <flavor>
                              The kernel flavor to run against: ('basic',
                              'gcov', 'notcmalloc')
                              [default: basic]
  -t <branch>, --teuthology-branch <branch>
                              The teuthology branch to run against.
                              [default: master]
  -m <type>, --machine-type <type>
                              Machine type [default: plana,mira,burnupi]
  -d <distro>, --distro <distro>
                              Distribution to run against
                              [default: ubuntu]
  --suite-branch <suite_branch>
                              Use this suite branch instead of the ceph branch
  --suite-dir <suite_dir>     Use this alternative directory as-is when
                              assembling jobs from yaml fragments. This causes
                              <suite_branch> to be ignored for scheduling
                              purposes, but it will still be used for test
                              running.

Scheduler arguments:
  --owner <owner>             Job owner
  -e <email>, --email <email>
                              When tests finish or time out, send an email
                              here. May also be specified in ~/.teuthology.yaml
                              as 'results_email'
  -N <num>, --num <num>       Number of times to run/queue the job
                              [default: 1]
  -l <jobs>, --limit <jobs>   Queue at most this many jobs
                              [default: 0]
  --subset <index/outof>      split suite into outof pieces and schedule index
                              piece
  -p <priority>, --priority <priority>
                              Job priority (lower is sooner)
                              [default: 1000]
  --timeout <timeout>         How long, in seconds, to wait for jobs to finish
                              before sending email. This does not kill jobs.
                              [default: 32400]
  --filter <string>           Only run jobs containing the string specified.
  --filter-out <string>       Do not run jobs containing the string specified.

"""


def main():
    args = docopt.docopt(doc)
    teuthology.suite.main(args)
