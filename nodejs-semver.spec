%{?scl:%scl_package nodejs-semver}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:       %{?scl_prefix}nodejs-semver
Version:        5.3.0
Release:        1%{?dist}
Summary:    Semantic versioner for npm
License:    ISC
URL:        https://github.com/isaacs/node-semver
Source0:    http://registry.npmjs.org/semver/-/semver-%{version}.tgz
BuildArch:  noarch
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
BuildRequires:  %{?scl_prefix}nodejs-devel

%description
The semantic version comparison library for the Node.js package manager (npm).

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/semver
cp -pr bin package.json semver.js %{buildroot}%{nodejs_sitelib}/semver

mkdir -p %{buildroot}%{_bindir}
ln -sf ../lib/node_modules/semver/bin/semver %{buildroot}%{_bindir}

%nodejs_symlink_deps

%files
%{nodejs_sitelib}/semver
%{_bindir}/semver
%doc README.md LICENSE

%changelog
* Thu Jan 05 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 5.3.0-1
- Updated with script

* Thu Jun 09 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 5.1.0-2
- Resolves: rhbz#1334856 , fixes wrong license

* Wed Feb 17 2016 Tomas Hrcka <thrcka@redhat.com> - 5.1.0-1
- Rebase to latest upstream

* Mon Nov 30 2015 Tomas Hrcka <thrcka@redhat.com> - 5.0.3-1
- Rebase to latest upstream

* Thu Jan 08 2015 Tomas Hrcka <thrcka@redhat.com> - 2.3.0-1
- New upstream release

* Tue Feb 04 2014 Tomas Hrcka <thrcka@redhat.com> - 2.1.0-3
- Upsteram license changed from MIT to BSD

* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 2.1.0-2
- replace provides and requires with macro

* Tue Jul 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.1.0-1
- new upstream release 2.1.0

* Fri Jul 12 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.0.10-1
- new upstream release 2.0.10

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.0.7-1
- new upstream release 2.0.7

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.4-3
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.4-2
- add macro for EPEL6 dependency generation

* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.1.4-2
- Add support for software collections

* Wed Mar 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.4-1
- new upstream release 1.1.4

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.3-1
- new upstream release 1.1.3

* Thu Jan 10 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.2-1
- new upstream release 1.1.2

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.1-2
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.1-1
- new upstream release 1.1.1
- clean up for submission

* Fri Apr 27 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.13-3
- guard Requires for F17 automatic depedency generation

* Sat Jan 21 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.13-2
- missing Group field for EL5

* Sat Jan 21 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.13-1
- new upstream release 1.0.13

* Thu Nov 17 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.11-1
- new upstream release 1.0.11

* Tue Oct 25 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.10-1
- new upstream release

* Mon Aug 22 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.9-1
- initial package
